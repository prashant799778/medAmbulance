import { Component, OnInit } from '@angular/core';
import { UserService } from '../services/user.service';
import { AppSettings } from '../utils/constant';

@Component({
  selector: 'app-dashboard',
  templateUrl: './dashboard.component.html',
  styleUrls: ['./dashboard.component.css']
})
export class DashboardComponent implements OnInit {
	reviewData = []
	driverData = []
	bookedTrip: any
	cancelTrip: any
	newUsers: any
	totalEarning: any
	constructor(public userService: UserService) { }

	ngOnInit() {
		let data = {
			'startLimit': 0,
			'endLimit': 10
		}
		this.userService.dataPostApi(data,AppSettings.dashboard).then(resp=>{
			if(resp['status'] == 'true'){
				
				this.driverData = resp['result']['driverDetails']
				this.bookedTrip = resp['result']['dashboard'].bookedTripCount
				this.cancelTrip = resp['result']['dashboard'].cancelledTripCount
				this.newUsers = resp['result']['dashboard'].newsUsers
				this.totalEarning = resp['result']['dashboard'].totalEarning
				console.log(this.driverData)
			}
		})
		// this.driverData = [
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

}
