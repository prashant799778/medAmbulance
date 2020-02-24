import { Component, OnInit } from '@angular/core';
import { UserService } from '../services/user.service';
import { AppSettings } from '../utils/constant';

@Component({
  selector: 'app-all-passengers',
  templateUrl: './all-passengers.component.html',
  styleUrls: ['./all-passengers.component.css']
})
export class AllPassengersComponent implements OnInit {
	tableHeading = [
		"No", "Name", "Mobile", "Email","Address", "Wallet Balance","Trip",
	]
	heading='All Passenger';
	loader: boolean;
	userData = [];
	constructor(public userService: UserService) { 
		this.loader = true;

	}

	ngOnInit() {
		this.getPassengerDetails()
	}

	getPassengerDetails(){
		// this.userService.getApiData(AppSettings.allusers).then(resp=>{
		// 	if(resp['status'] == 'true'){
		// 		this.userData = resp['result']
		// 		this.loader = false
		// 	}
			
		// })
		this.userData = [
							{	'name':'Vijay Pal',
								'mobileNo': 8888517655,
								'email': 'vijay@gmail.com',
								'currentLocation': 'Noida UP-87',
								'wallet': 100,
								'tripCount': 10,
								'status': 1
							},
							{	'name':'Vijay Pal',
								'mobileNo': 8888517655,
								'email': 'vijay@gmail.com',
								'currentLocation': 'Noida UP-87',
								'wallet': 100,
								'tripCount': 10,
								'status': 1
							},
							{	'name':'Vijay Pal',
								'mobileNo': 8888517655,
								'email': 'vijay@gmail.com',
								'currentLocation': 'Noida UP-87',
								'wallet': 100,
								'tripCount': 10,
								'status': 1
							}
						]
	}
	getStatus(status){
		if(status == 0){
			return 'ACTIVE'
		}else if(status == 1){
			return 'DEACTIVE'
		}
	}

}
