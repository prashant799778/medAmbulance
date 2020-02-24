import { Component, OnInit } from '@angular/core';
import { UserService } from 'src/app/services/user.service';
import { Router } from '@angular/router';
import { AppSettings } from 'src/app/utils/constant';
declare var jQuery: any;

@Component({
  selector: 'app-all-responder',
  templateUrl: './all-responder.component.html',
  styleUrls: ['./all-responder.component.css']
})
export class AllResponderComponent implements OnInit {
	 
	driverData= []
	errorMessage: boolean
	messageShow: any;
	loader: boolean;
	activatedds: boolean;
	driverID: any;
	constructor(public userService: UserService,
				public router: Router) { 
		this.errorMessage = false;
		this.loader = true;
		this.activatedds
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
		this.userService.dataPostApi(data,AppSettings.alldriver).then(resp=>{
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
		this.router.navigate(['/responder/viewResponder'],{queryParams: {driverId : id, view: view}})
	}
	deleteDriver(id){
		this.userService.deleteData('Responder',id)
		
		jQuery('#deleteModal').modal('show')
	}


	VerifyDriver(){
		let data = {
			'driverId': this.driverID
		}
		this.userService.dataPostApi(data,AppSettings.updateDriverStatus).then(resp=>{
			if(resp['status'] == 'true'){
				let data = {
					'startLimit': 0,
					'endLimit': 10
				}
				this.userService.dataPostApi(data,AppSettings.alldriver).then(resp=>{
					if(resp['status'] == 'true'){
				
						this.errorMessage = false;
						this.driverData = resp['result']
						this.loader = false;
					}else{
							this.errorMessage = true;
							this.messageShow = resp['message']
							this.loader = false;
					}		
				})
				this.activatedds = true;
				setTimeout(() => {
					jQuery('#verifiyModal').modal('hide')
					setTimeout(()=>{
						this.activatedds = false;
					},1000)
				}, 2000);
			}
		})
	}
	verifiedDriver(id){
		this.driverID = id;
		jQuery('#verifiyModal').modal('show')
	}
	closeModal(){
		jQuery('#verifiyModal').modal('hide')
	}

}

