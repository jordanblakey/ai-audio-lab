class AudioProcessor extends AudioWorkletProcessor {
  process(inputs, outputs, parameters) {
    const input = inputs[0];
    if (input.length > 0) {
      const channelData = input[0];
      // We send a copy of the buffer to avoid issues with SharedArrayBuffer or neutered buffers
      this.port.postMessage(channelData.slice());
    }
    return true;
  }
}

registerProcessor('audio-processor', AudioProcessor);
