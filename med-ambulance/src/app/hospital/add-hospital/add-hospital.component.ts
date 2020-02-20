import { Component, OnInit } from '@angular/core';
import { UserService } from 'src/app/services/user.service';
import { Router } from '@angular/router';
import { AppSettings } from 'src/app/utils/constant';
declare var jQuery: any;

@Component({
  selector: 'app-add-hospital',
  templateUrl: './add-hospital.component.html',
  styleUrls: ['./add-hospital.component.css']
})
export class AddHospitalComponent implements OnInit {
	driverData= []
	errorMessage: boolean
	messageShow: any;
	loader: boolean;
	constructor(public userService: UserService,
				public router: Router) { 
		this.errorMessage = false;
		this.loader = true;
	}

	ngOnInit() {
		this.userService.driverEventEmit.subscribe(()=>{
			this.getDriverData()
		})
		this.getDriverData()
	}

	getDriverData(){
		let data = {
			'startLimit': 0,
			'endLimit': 10
		}
		this.userService.dataPostApi(data,AppSettings.allHospital).then(resp=>{
			if(resp['status'] == 'true'){
				
				this.errorMessage = false;
				this.driverData = resp['result']
				this.loader = false;
			}else{
					this.errorMessage = true;
					this.messageShow = resp['message']
					this.loader = false;
				// 	this.driverData = [
				// 	{	'name':'Vijay Pal',
				// 		'mobileNo': 8888517655,
				// 		'email': 'vijay@gmail.com',
				// 		'currentLocation': 'Noida UP-87',
				// 		'wallet': 100,
				// 		'dateCreate': '02/10/2015',
				// 		'tripCount': 10,
				// 		'status': 1
				// 	},
				// 	{	'name':'Vijay Pal',
				// 		'mobileNo': 8888517655,
				// 		'email': 'vijay@gmail.com',
				// 		'currentLocation': 'Noida UP-87',
				// 		'wallet': 100,
				// 		'dateCreate': '02/10/2015',
				// 		'tripCount': 10,
				// 		'status': 0
				// 	},
				// 	{	'name':'Vijay Pal',
				// 		'mobileNo': 8888517655,
				// 		'email': 'vijay@gmail.com',
				// 		'currentLocation': 'Noida UP-87',
				// 		'wallet': 100,
				// 		'dateCreate': '02/10/2015',
				// 		'tripCount': 10,
				// 		'status': 2
				// 	}
				// ]
			}
		})
		
	}

	getStatus(status){
		if(status == 0){
			return 'ON TRIP'
		}else if(status == 1){
			return 'AVAILABLE'
		}else if(status == 2){
			return 'LEAVE'
		}

	}

	editDriver(id,view){
		console.log(id)
		this.router.navigate(['/driver/editDriver'],{queryParams: {driverId : id, view: view}})
	}
	deleteDriver(id){
		this.userService.deleteData('Driver',id)
		
		jQuery('#deleteModal').modal('show')
	}

}