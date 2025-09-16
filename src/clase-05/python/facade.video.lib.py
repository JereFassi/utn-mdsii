# Subsistema complejo (simulado)
class VideoReader: 
    def read(self, path): return f"raw({path})"

class VideoFilter:
    def denoise(self, raw): return f"denoised({raw})"

class VideoEncoder:
    def encode(self, stream, fmt): return f"encoded[{fmt}]({stream})"

# Facade
class VideoConverter:
    def encode(self, filename: str, target_format: str) -> str:
        reader = VideoReader()
        vf = VideoFilter()
        enc = VideoEncoder()
        raw = reader.read(filename)
        clean = vf.denoise(raw)
        return enc.encode(clean, target_format)

# Cliente
if __name__ == "__main__":
    api = VideoConverter()
    print(api.encode("cats.mov", "mp4"))  # encoded[mp4](denoised(raw(cats.mov)))
