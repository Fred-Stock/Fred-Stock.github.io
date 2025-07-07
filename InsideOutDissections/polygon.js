class polygon{

	constructor(_n, _sidel){
		this.n = _n;
		this.side_l = _sidel;
		this.angle = (Math.PI) - (Math.PI)*((this.n-2)/this.n);
	}

	draw(sketch, x, y){
	
		let x1 = x;// - this.side_l/2;
		let y1 = y;// - this.side_l/2;
		let x2 = x1 + this.side_l;
		let y2 = y1;
		let total_rot = 0;

		for( let i = 0; i < this.n; i++){
			sketch.line(x1, y1, x2, y2);
			// sketch.square(x1-5,y1-5,10);
			x1 = x2;
			y1 = y2;
			x2 = x2 + Math.cos(this.angle + total_rot)*this.side_l;
			y2 = y2 + Math.sin(this.angle + total_rot)*this.side_l;
			total_rot += this.angle;
		}
	}

}

class k_gon{

	constructor(_k, _sidel, _polyn){
		this.n          = 2*_k + 2;
		if(_k == 1){
			this.n = 3;
		}
		this.k          = _k;
		this.side_l     = _sidel;
		this.poly_angle = Math.PI - (Math.PI)*((_polyn-2)/_polyn);
		this.end_angle  = Math.PI - (2*Math.PI)*(this.k-1)/_polyn;
	} 

	draw(sketch, x, y, init_angle){
		
		if(this.n == 3){
			let x1 = x - Math.cos(init_angle - this.poly_angle) * this.side_l;
			let y1 = y - Math.sin(init_angle - this.poly_angle) * this.side_l;
			// sketch.square(x1-5, y1-5, 10);
			let x2 = x1 + Math.cos(Math.PI / 3 + (init_angle - this.poly_angle)) * this.side_l;
			let y2 = y1 + Math.sin(Math.PI / 3 + (init_angle - this.poly_angle)) * this.side_l;


			sketch.triangle(x, y, x1, y1, x2, y2);
		}
		else{

			let x1 = x;
			let y1 = y;
			let x2 = x1 + this.side_l*Math.cos(init_angle);
			let y2 = y1 + this.side_l*Math.sin(init_angle);
		
			let total_rot = init_angle;

			for( let i = 0; i < 2; i++){
				for(let j = 0; j < this.k - 1; j++){
				
					sketch.line(x1, y1, x2, y2);
					x1 = x2;
					y1 = y2;
					x2 = x2 + Math.cos(this.poly_angle + total_rot)*this.side_l;
					y2 = y2 + Math.sin(this.poly_angle + total_rot)*this.side_l;

					total_rot += this.poly_angle;
				}
				total_rot -= this.poly_angle;
				// Have to undo the last addition to x2 and y2
				x2 = x1 + Math.cos(this.end_angle + total_rot) * this.side_l;
				y2 = y1 + Math.sin(this.end_angle + total_rot) * this.side_l;
				sketch.line(x1, y1, x2, y2);
				total_rot += this.end_angle;

				x1 = x2;
				y1 = y2;
				x2 = x2 + Math.cos(this.poly_angle + total_rot)*this.side_l;
				y2 = y2 + Math.sin(this.poly_angle + total_rot)*this.side_l;
				total_rot += this.poly_angle;
			}
		}
	}

}

class divided_poly{

	constructor(_n, _ks, _sidel){
	
		this.n      = _n;
		this.ks     = _ks;
		this.side_l = _sidel;


		this.polys  = this.create();

	}

	create(){

		let poly = new polygon(this.n, this.side_l);
		let polys = [poly];

		for(let i = 0; i < this.ks.length; i++){
	
			let k = this.ks[i];
			polys.push(new k_gon(k, this.side_l, this.n));

		}
		return polys;
	
	}

	draw(sketch, _x, _y){

		let x = _x;
		let y = _y;


		

		let total_rot = 0;
		
		let int_angle = Math.PI - (Math.PI)*(this.n-2)/this.n;

		for( let i = 1; i < this.polys.length; i++){
		if(i > 1){
			total_rot += int_angle;
		}
			sketch.stroke(255*(i%3), 255*((i+1)%3), 0);
			// sketch.circle(x, y, 10);

			this.polys[i].draw(sketch, x, y, total_rot);

			x += Math.cos(total_rot)*this.side_l;

			y += Math.sin(total_rot)*this.side_l;


			for( let j = 1; j < this.ks[i-1]; j++){

				total_rot += int_angle;			

				x += Math.cos(total_rot)*this.side_l;
				y += Math.sin(total_rot)*this.side_l;
	
			}
		}
		sketch.stroke(0,0,0);

		this.polys[0].draw(sketch, x, y);


	//	console.log("-------------------------");
	}

}
