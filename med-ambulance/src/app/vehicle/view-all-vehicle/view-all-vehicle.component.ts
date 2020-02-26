import { Component, OnInit } from '@angular/core';
import { UserService } from 'src/app/services/user.service';
import { AppSettings } from 'src/app/utils/constant';

@Component({
  selector: 'app-view-all-vehicle',
  templateUrl: './view-all-vehicle.component.html',
  styleUrls: ['./view-all-vehicle.component.css']
})
export class ViewAllVehicleComponent implements OnInit {
	vehicleData = []
	loader: boolean;
	totalRecords: any;
	pageSize: any = 10;
	paginationDisplay: boolean;
	constructor(public userService: UserService) {
		this.loader = true;
	 }

	ngOnInit() {
		this.getVehicleData()
	}

	getVehicleData(){
		let data = {
			'endlimit': 10,
			'startlimit': 0
		}
		this.userService.dataPostApi(data,AppSettings.allAmbulance).then(resp=>{
			if(resp['status'] == 'true'){
				this.totalRecords = resp['totalCount']
				this.vehicleData = resp['result']
				this.loader = false;
				if(this.totalRecords > this.pageSize){
					this.paginationDisplay = true;
				}else{
					this.paginationDisplay = false;
				}
			}
		})
		// this.vehicleData = [
		// 	{	'image': 'http://radixtouch.in/templates/templatemonster/ecab/source/assets/img/dp.jpg',
		// 		'fuelType':'CNG',
		// 		'purchaseDate': 2020,
		// 		'regNumber': 'UP87H9315',
		// 		'category': 'GOV',
		// 		'type': 'ALS',
		// 		'modal': 'Car',
				
		// 	},
		// 	{	'image': 'http://radixtouch.in/templates/templatemonster/ecab/source/assets/img/user/usrbig5.jpg',
		// 		'fuelType':'CNG',
		// 		'purchaseDate': 2020,
		// 		'regNumber': 'UP87H9315',
		// 		'category': 'GOV',
		// 		'type': 'ALS',
		// 		'modal': 'Car',
				
		// 	},
		// 	{	'image': 'http://radixtouch.in/templates/templatemonster/ecab/source/assets/img/user/usrbig7.jpg',
		// 		'fuelType':'CNG',
		// 		'purchaseDate': 2020,
		// 		'regNumber': 'UP87H9315',
		// 		'category': 'GOV',
		// 		'type': 'ALS',
		// 		'modal': 'Car',
				
		// 	}
		// ]
	}

	pageChanged(event){
		let endlimit = this.pageSize;
		let startlimit = (this.pageSize * event) - this.pageSize;
		if(endlimit > this.totalRecords){
			endlimit = this.totalRecords;
			console
			// this.frmShowNews.get('endlimit').setValue(endlimit)
		}else{
			endlimit = this.pageSize
		}
		// this.frmShowNews.get('startlimit').setValue(startlimit)
		let data = {
			'endlimit': endlimit,
			'startlimit': startlimit
		}
		this.userService.dataPostApi(data,AppSettings.allAmbulance).then((data: any[]) => {
			this.totalRecords = data['totalCount']
			if(this.totalRecords > this.pageSize){
				this.paginationDisplay = true;
			}else{
				this.paginationDisplay = false;
			}
			this.vehicleData = data['result']
			this.loader = false;
			
		});
	} 
	
}
