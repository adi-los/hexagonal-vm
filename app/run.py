import uvicorn
import os

PORT = int(os.environ.get('PORT', 8000))

def main():
    uvicorn.run("vm_api.app.main:app", host="127.0.0.1", port=PORT, reload=True)

if __name__ == "__main__":
    main()
