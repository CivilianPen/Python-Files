mj = false;
j = false;
pipes = []
spawnRate = 100
Rate = spawnRate-10
Score = 0
gameover = false
SizeOfSpace = {0:350,1:340,2:330,3:320,4:310,5:300,6:290,7:280,8:270,9:260,10:250,11:240,12:230,13:220,14:210,15:200,16:190}
BestScore = 0
function preload() {
}
function keyPressed(){
  if (key === 'Escape'){
    if (gameover == true){
      frameRate(60)
      gameover = false
      setup()
    }
    else{
        Pause()
    }
  }
}
function setup() {
  createCanvas(1100, 700);
  frameRate(60);
  bird = new Bird();
  pipes = []
  Score = 0
  Rate = spawnRate-10
}

function draw() {
  background(220);
  bird.show();
  if ((keyIsDown(32) || keyIsDown(UP_ARROW) ||  mouseIsPressed)) {
    j = true
  }
  for (let i = 0; i < pipes.length; i++) {
    pipes[i].show();
  }
  Rate+=1
  if (Rate == spawnRate){
    t1 = round(random(100,300))
    if(Math.floor(Score / 5)<=16){
      pipes.push(new Pipe(1100, t1, height-t1-SizeOfSpace[Math.floor(Score / 5)] ))
    }
    else{
      pipes.push(new Pipe(1100, t1, height-t1-SizeOfSpace[16] ))
    }
    Rate = 0
  }
  
  truepipes = []
  for(let i = 0; i<pipes.length; i++){
    if (pipes[i].x >= -180){
      truepipes.push(pipes[i])
    }
  }
  pipes = truepipes
  if (gameover == false){
      fill(0)
     textSize(50)
    text(Score,(width/2),(height/3)-(3*textSize()))
    textSize(30)
    text('Best: '+BestScore,15,35)
  }
 else{
   GameOver()
 }

}

class Bird{
  constructor(){
    this.x = 250;
    this.y = 350;
    this.js = 20;
    this.size = 100;
    this.speed = 5;
  }
  show(){
	fill('yellow')
    	rect(this.x, this.y, this.size, this.size)

    
      if (j == true) {
        this.js = 10;
        j = false;
        mj = true;
      }
      if (this.y<=0){
        this.js = -2;
        mj = true;
      }
      this.y -= this.js;
      this.js -= 1.1;
      if (this.y >= height-80) {
        this.y = height-80;
        mj = false;
        this.js = 0;
      }
  }
}
class Pipe {
  constructor(x, size_1 , size_2) {
    this.x = x;
    this.size1 = size_1;
    this.size2 = size_2;
    this.wide = 180;
  }
  show() {
    fill('green')
    rect(this.x,0 ,this.wide,this.size1)
    rect(this.x,height-this.size2 ,this.wide,this.size2)
      this.x -= bird.speed
      if(this.x+(this.wide/2) == bird.x){
        Score+=1
      }
      if((this.x<bird.x+bird.size && bird.y+21<this.size1 && this.x+this.wide>bird.x) || (this.x<bird.x+bird.size && bird.y+bird.size-21>height-this.size2 && this.x+this.wide>bird.x)){
         gameover = true
      }
  }
}
function GameOver(){
    gameover = true
    BestScore = Score
    frameRate(0)
    fill(0,0,0,187)
    rect(0,0,width,height)
    fill(255)
    textSize(80)
    text('LOST',(width/2)-(1.2*textSize()),(height/2)-(3*textSize()))
    textSize(50)
    text('Current: '+Score,(width/2)-(2*textSize())-5,(height/3)-(1*textSize()))
    textSize(50)
    text('Best:      '+BestScore,(width/2)-(2*textSize())-5,(height/3)-(1*textSize())+50)
    textSize(30)
    text('press esc button to resume the game',(width/2)-(8*textSize()),(height/2)-(1*textSize()))
  
}
function Pause(){
  
}