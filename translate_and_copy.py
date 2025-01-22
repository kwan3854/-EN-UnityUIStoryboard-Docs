import os
import shutil
import requests
import logging
from pathlib import Path
import time
from typing import Optional

# 로깅 설정.
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class TranslationError(Exception):
    """번역 과정에서 발생하는 예외 처리 클래스"""
    pass

def setup_directories() -> tuple[Path, Path]:
    """작업 디렉토리 설정"""
    source_path = Path.cwd()  # 현재 작업 디렉토리
    target_path = source_path / "english-repo"  # 번역 파일을 저장할 대상 디렉토리
    
    logger.info(f"소스 디렉토리: {source_path}")
    logger.info(f"대상 디렉토리: {target_path}")
    
    return source_path, target_path

def translate_text(text: str, api_key: str, retries: int = 3) -> Optional[str]:
    """DeepL API를 사용한 텍스트 번역"""
    for attempt in range(retries):
        try:
            response = requests.post(
                url="https://api.deepl.com/v2/translate",
                data={
                    "auth_key": api_key,
                    "text": text,
                    "target_lang": "EN",
                    "source_lang": "KO"
                },
                timeout=30
            )
            
            if response.status_code == 200:
                return response.json()["translations"][0]["text"]
            elif response.status_code == 429:  # Rate limit
                wait_time = min(2 ** attempt, 60)
                logger.warning(f"Rate limit hit. Waiting {wait_time} seconds...")
                time.sleep(wait_time)
                continue
            else:
                logger.error(f"Translation API error: {response.status_code} - {response.text}")
                raise TranslationError(f"번역 API 오류: {response.status_code}")
                
        except requests.exceptions.RequestException as e:
            if attempt == retries - 1:
                raise TranslationError(f"네트워크 오류: {str(e)}")
            time.sleep(2 ** attempt)
            
    return None

def should_process_file(file_path: Path) -> bool:
    """처리해야 할 파일인지 확인"""
    IGNORED_PATTERNS = {'.git', '.github', 'node_modules', '__pycache__', 'english-repo'}
    return not any(pattern in str(file_path) for pattern in IGNORED_PATTERNS)

def should_translate(file_path: Path) -> bool:
    """번역이 필요한 파일인지 확인"""
    TRANSLATE_EXTENSIONS = {'.md', '.txt'}
    return file_path.suffix.lower() in TRANSLATE_EXTENSIONS

def get_target_path(file_path: Path, source_root: Path, target_root: Path) -> Path:
    """소스 파일의 대상 경로 계산"""
    relative_path = file_path.relative_to(source_root)
    return target_root / relative_path

def main():
    try:
        api_key = os.environ.get("DEEPL_API_KEY")
        if not api_key:
            raise ValueError("DEEPL_API_KEY 환경 변수가 설정되지 않았습니다.")

        source_path, target_path = setup_directories()
        
        for source_file in source_path.rglob('*'):
            if not should_process_file(source_file):
                continue
            
            target_file = get_target_path(source_file, source_path, target_path)
            
            if source_file.is_dir():
                target_file.mkdir(parents=True, exist_ok=True)
                continue
            
            if should_translate(source_file):
                with open(source_file, "r", encoding="utf-8") as f:
                    text = f.read()
                translated_text = translate_text(text, api_key)
                if translated_text:
                    target_file.parent.mkdir(parents=True, exist_ok=True)
                    with open(target_file, "w", encoding="utf-8") as f:
                        f.write(translated_text)
                else:
                    logger.error(f"파일 번역 실패: {source_file}")
            else:
                shutil.copy2(source_file, target_file)

        # .gitbook 폴더 복사
        gitbook_source_path = source_path / ".gitbook"
        gitbook_target_path = target_path / ".gitbook"
        if gitbook_source_path.exists():
            shutil.copytree(gitbook_source_path, gitbook_target_path, dirs_exist_ok=True)

    except Exception as e:
        logger.error(f"스크립트 실행 중 오류 발생: {str(e)}")
        raise

if __name__ == "__main__":
    main()