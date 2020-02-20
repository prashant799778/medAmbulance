import { Component, OnInit } from '@angular/core';
import { UserService } from 'src/app/services/user.service';
import { AppSettings } from 'src/app/utils/constant';

@Component({
  selector: 'app-active-trip',
  templateUrl: './active-trip.component.html',
  styleUrls: ['./active-trip.component.css']
})
export class ActiveTripComponent implements OnInit {
	tableHeading = [
		"No", "Trip Id", "Driver Name", "Passenger Name","Trip From", "Trip To","Start Time"
	]
	heading='Active Trip'
	activeTripData = []
	constructor(public userService: UserService) { }

	ngOnInit() {
		this.getActiveTripData()	
	}

	getActiveTripData(){
		let data = {
			'startLimit': 0,
			'endLimit': 10
		}
		this.userService.dataPostApi(data,AppSettings.ActiveTrip).then(resp=>{
			console.log(resp)
		})
		// this.activeTripData = [
		// 	{
		// 		'tripId': 1765,
		// 		'driverName': 'Hemant Gusain',
		// 		'userName': 'Vijay Pal',
		// 		'tripFrom': 'Noida',
		// 		'tripTo': 'Agra',
		// 		'startTime': '02:00pm',
				
		// 	},
		// 	{
		// 		'tripId': 1165,
		// 		'driverName': 'Hemant Gusain',
		// 		'userName': 'Vijay Pal',
		// 		'tripFrom': 'Noida',
		// 		'tripTo': 'Agra',
		// 		'startTime': '02:00pm',
				
		// 	},
		// 	{
		// 		'tripId': 1865,
		// 		'driverName': 'Hemant Gusain',
		// 		'userName': 'Vijay Pal',
		// 		'tripFrom': 'Noida',
		// 		'tripTo': 'Agra',
		// 		'startTime': '02:00pm',
				
		// 	}
		// ]
	}

}
