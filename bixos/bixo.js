class Bixo {
  constructor(ix, iy, ir) {
    this.name = random(["Jox", "Chul", "Nico"]);
    this.pos = {
      x: ix,
      y: iy
    };
    this.rad = ir;
    this.dir = random(TAU);
    this.angvel = random(0, PI / 16);
    this.linvel = random(1, 2);
    this.health = 100;
    this.hue = 0;
  }
  edges() {
    if (this.pos.x <= 0) {
      this.pos.x = width;
    } else if (this.pos.x >= width) {
      this.pos.x = 0;
    }
    if (this.pos.y <= 0) {
      this.pos.y = height;
    } else if (this.pos.y >= height) {
      this.pos.y = 0;
    }
  }
  show() {
    this.hue = map(0, 0, 100, 0, 360);
    push();
    stroke(this.hue, 100, 50);
    strokeWeight(2);
    fill(this.hue, 100, 25);
    translate(this.pos.x, this.pos.y);
    rotate(this.dir);
    beginShape();
    vertex(1 * this.rad, 0 * this.rad);
    vertex(0 * this.rad, 0.7 * this.rad);
    vertex(-1 * this.rad, 0.5 * this.rad);
    vertex(-0.5 * this.rad, 0 * this.rad);
    vertex(-1 * this.rad, -0.5 * this.rad);
    vertex(0 * this.rad, -0.7 * this.rad);
    endShape(CLOSE);
    strokeWeight(5);
    point(0, 0);
    pop();
  }
  rotate() {
    this.dir += this.angvel;
  }
  forward() {
    this.pos.x += this.linvel * cos(this.dir);
    this.pos.y += this.linvel * sin(this.dir);
  }
  decay() {
    this.size -= 0.001;
  }
}