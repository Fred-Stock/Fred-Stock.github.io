STATES = {
	"init":0,
	"cut_pieces":1,
	"rotate_pieces":2,
}


var canvasW = window.screen.width*.99;
var canvasH = window.screen.height*.8;
var side_l = 10;
var draw = false;

var g_n = -1;
var g_ks = [];

var scene = function(sketch){
    
    sketch.setup = function(){

	    var canv = sketch.createCanvas(canvasW, canvasH);
	    canv.position(0,30);
   
    }
    
    sketch.draw = function(){
		if(!draw){
			return;
		}
	    sketch.background(255, 255, 255);
	    state = 1;
	    switch(state){
		case 0:
			
			   // let angle = (Math.PI/2) * (n-2)/n;
			    /*(let x1 = canvasW/4;
			    let y1 = canvasH/4;

			    let x2 = x1 + side_l;
			    let y2 = y1;
			    for( let i = 0; i < n; i++){
				    sketch.line(x1, y1, x2, y2);
				    x1 = x2;
				    y1 = y2;
				    x2 = x2 + Math.cos((i+1)*angle)*side_l;
				    y2 = y2 + Math.sin((i+1)*angle)*side_l;
				}
*/
			    let poly = new polygon(n, side_l);
			    poly.draw(sketch, canvasW/4, canvasH/4);
			    

			   		break;
				case 1:
			   
			    let sub_poly = new divided_poly(g_n, g_ks, side_l);
			    sub_poly.draw(sketch, canvasW/8, canvasH/8);

			    	break;
				case 2:
			    	break;
				default:
   					break; 
		}
   
	}
}
new p5(scene);

function start(){
	let n = parseInt(document.getElementById("n").value);
	side_l = 1200/n;

	// let kString = document.getElementById("ks").value;
	let kString = "";
	let ks = [];
	if (kString == ""){
		let k   = Math.floor((n - 4)/2 + 1);
		let rem = n;
		for(; k <= rem; rem -= k){
			ks.push(k);
		}
		if( rem > 0){
			ks.push(rem);
		}
	}
	else{
		kString = kString.split(",");
		ks = kString.map((x) => parseInt(x));
	}

	g_n = n;
	g_ks = ks;
	draw = true;


}
