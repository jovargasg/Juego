let bixos = [];
let maxb = 10;
let buSave;

function setup() {
  createCanvas(windowWidth, windowHeight);
  colorMode(HSL);
  for (let i = 0; i < maxb; i++) {
    bixos[i] = new Bixo(random(width), random(height), 25);
  }
  buSave = createButton("Save Bixo 0");
  buSave.mousePressed(saveBixo)
}

function draw() {
  background(0, 0, 0, 0.2);
  for (let i = 0; i < bixos.length; i++) {
    bixos[i].show();
    //bixos[i].decay();
    //bixos[i].forward();
    //bixos[i].rotate();
    bixos[i].edges();
    if (bixos[i].size <= 0.1) {
      bixos.splice(i, 1);
    }
  }
  if (bixos.length <= maxb) {
    let b = new Bixo(random(width), random(height), 25, random(TAU));
    bixos.push(b);
  }
}

function saveBixo() {
  saveJSON(bixos[0], "bixo.json")
}