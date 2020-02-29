import { Component, OnInit } from '@angular/core';
import { UserService } from '../services/user.service';
import { AppSettings } from '../utils/constant';
import { Router } from '@angular/router';
declare var jQuery: any;

@Component({
  selector: 'app-dashboard',
  templateUrl: './dashboard.component.html',
  styleUrls: ['./dashboard.component.css']
})
export class DashboardComponent implements OnInit {
	reviewData = []
	driverData = []
	driverID: any;
	bookedTrip: any
	cancelTrip: any
	newUsers: any
	totalEarning: any
	loader: boolean;
	activatedds: boolean;
	errorMessage: any;
	messageShow: any;
	userImage: any;
	constructor(public userService: UserService,
				public router: Router) {
					this.loader = true;
					console.log(console.log("vijay"))
				}

	ngOnInit() {
		
		let data = {
			'startLimit': 0,
			'endLimit': 5
		}
		this.userService.dataPostApi(data,AppSettings.dashboard).then(resp=>{
			if(resp['status'] == 'true'){
				
				this.driverData = resp['result']['driverDetails']
				this.bookedTrip = resp['result']['dashboard'].bookedTripCount
				this.cancelTrip = resp['result']['dashboard'].cancelledTripCount
				this.newUsers = resp['result']['dashboard'].newsUsers
				this.totalEarning = resp['result']['dashboard'].totalEarning
				console.log(this.driverData)
				this.userImage = this.driverData[0].profilePic;
				
				this.loader = false;
			}
		})
		
		this.reviewData = 	[ 
			{
				'userImage': 'http://radixtouch.in/templates/templatemonster/ecab/source/assets/img/user/usrbig1.jpg',
				'name': 'Nisha',
				'review':'Good Serivces',
				'email': 'nisha@gmail.com',
				'star': 4
			},
			{
				'userImage': 'http://radixtouch.in/templates/templatemonster/ecab/source/assets/img/user/usrbig1.jpg',
				'name': 'Vijay',
				'review':'Good Serivces',
				'email': 'nisha@gmail.com',
				'star': 4
			},
			{
				'userImage': 'http://radixtouch.in/templates/templatemonster/ecab/source/assets/img/user/usrbig1.jpg',
				'name': 'Hemant',
				'review':'Good Serivces',
				'email': 'nisha@gmail.com',
				'star': 4
			}
		]
	}

	// getStatus(status){
	// 	if(status == 0){
	// 		return 'ON TRIP'
	// 	}else if(status == 1){
	// 		return 'AVAILABLE'
	// 	}else if(status == 2){
	// 		return 'LEAVE'
	// 	}

	// }
	editDriver(id,view){
		console.log(id)
		this.router.navigate(['/driver/editDriver'],{queryParams: {driverId : id, view: view}})
	}

	verifiedDriver(id){
		this.driverID = id;
		jQuery('#verifiyModalD').modal('show')
	}
	closeModal(){
		jQuery('#verifiyModalD').modal('hide')
	}
	VerifyDriver(){
		this.loader = true;
		let data = {
			'driverId': this.driverID
		}
		this.userService.dataPostApi(data,AppSettings.dashboard).then(resp=>{
			if(resp['status'] == 'true'){
				let data = {
					'startLimit': 0,
					'endLimit': 5
				}
				this.userService.dataPostApi(data,AppSettings.dashboard).then(resp=>{
					if(resp['status'] == 'true'){
				
						this.errorMessage = false;
						this.driverData = resp['result']['driverDetails']
				this.bookedTrip = resp['result']['dashboard'].bookedTripCount
				this.cancelTrip = resp['result']['dashboard'].cancelledTripCount
				this.newUsers = resp['result']['dashboard'].newsUsers
				this.totalEarning = resp['result']['dashboard'].totalEarning
						this.loader = false;
					}else{
							this.errorMessage = true;
							this.messageShow = resp['message']
							this.loader = false;
					}		
				})
				this.activatedds = true;
				setTimeout(() => {
					jQuery('#verifiyModalD').modal('hide')
					setTimeout(()=>{
						this.activatedds = false;
					},1000)
				}, 2000);
			}
		})
	}
	deleteDriver(id){
		this.userService.deleteData('Driver',id)
		
		jQuery('#deleteModal').modal('show')
	}
	

}
