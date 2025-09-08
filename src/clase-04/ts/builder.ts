// Clase 4 — Patrones Creacionales
// Ejemplo: Builder (TypeScript)
// --------------------------------

class Computer {
  cpu?: string;
  ram?: string;
  storage?: string;
  gpu?: string;

  toString(): string {
    return `Computer(cpu=${this.cpu}, ram=${this.ram}, storage=${this.storage}, gpu=${this.gpu})`;
  }
}

class ComputerBuilder {
  private computer: Computer;

  constructor() {
    this.computer = new Computer();
  }

  addCPU(cpu: string): this {
    this.computer.cpu = cpu;
    return this;
  }

  addRAM(ram: string): this {
    this.computer.ram = ram;
    return this;
  }

  addStorage(storage: string): this {
    this.computer.storage = storage;
    return this;
  }

  addGPU(gpu: string): this {
    this.computer.gpu = gpu;
    return this;
  }

  build(): Computer {
    return this.computer;
  }
}

// Uso
const builder = new ComputerBuilder();
const gamingPC = builder
  .addCPU("Intel i9")
  .addRAM("32GB")
  .addStorage("1TB SSD")
  .addGPU("NVIDIA RTX 4080")
  .build();

console.log(gamingPC.toString());
