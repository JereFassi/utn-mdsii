// Subsistema complejo (simulado)
class VideoReader { read(path: string) { return `raw(${path})`; } }
class VideoFilter { denoise(raw: string) { return `denoised(${raw})`; } }
class VideoEncoder { encode(stream: string, fmt: string) { return `encoded[${fmt}](${stream})`; } }

// Facade
class VideoConverter {
  encode(filename: string, targetFormat: string): string {
    const reader = new VideoReader();
    const filter = new VideoFilter();
    const encoder = new VideoEncoder();
    const raw = reader.read(filename);
    const clean = filter.denoise(raw);
    return encoder.encode(clean, targetFormat);
  }
}

// Cliente
const api = new VideoConverter();
console.log(api.encode("cats.mov", "mp4"));
