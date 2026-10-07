// A generation identifies one applied settings set. A request identifies one
// operation within it. Invalidation never lets an old reply clear a new request.
export class RequestGate {
  constructor() {
    this.generation = 0;
    this.nextRequestId = 0;
    this.pending = null;
  }
  get busy() {
    return this.pending !== null;
  }
  invalidate() {
    this.generation++;
    this.pending = null;
  }
  issue(payload) {
    const request = {
      ...payload,
      generation: this.generation,
      requestId: ++this.nextRequestId,
    };
    this.pending = request.requestId;
    return request;
  }
  accept(reply) {
    if (
      reply.generation !== this.generation ||
      reply.requestId !== this.pending
    )
      return false;
    this.pending = null;
    return true;
  }
}
