from pathlib import Path

BASE_DIR = Path(__file__).parent       
path = BASE_DIR / "data.txt"           

path.exists()                      
path.read_text(encoding="utf-8") 
path.write_text("текст", encoding="utf-8")
path.parent.mkdir(parents=True, exist_ok=True)
path.name, path.suffix               


with open("data.txt","w", encoding="utf-8") as f:
    f.write("Hello")