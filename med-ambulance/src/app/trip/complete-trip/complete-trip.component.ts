import { Component, OnInit } from '@angular/core';
import { UserService } from 'src/app/services/user.service';
import { AppSettings } from 'src/app/utils/constant';

@Component({
  selector: 'app-complete-trip',
  templateUrl: './complete-trip.component.html',
  styleUrls: ['./complete-trip.component.css']
})
export class CompleteTripComponent implements OnInit {
	tableHeading = [
		"No", "Trip Id", "Driver Name", "Passenger Name","Trip From", "Trip To","Start Time","End Time","Distance","Fare","View Route"
	]
	heading='Complete Trip'
	completeTripData = []
	constructor(public userService: UserService) { }

	ngOnInit() {
		this.getBookTrip()
	}

	getBookTrip(){
		let data = {
			'startLimit': 0,
			'endLimit': 10
		}
		// this.userService.dataPostApi(data,AppSettings.CompeltedTrip).then(resp=>{
		// 	console.log(resp)
		// })
		this.completeTripData = [
			{
				'tripId': 1765,
				'driverName': 'Hemant Gusain',
				'userName': 'Vijay Pal',
				'tripFrom': 'Noida',
				'tripTo': 'Agra',
				'startTime': '02:00pm',
				
			},
			{
				'tripId': 1165,
				'driverName': 'Hemant Gusain',
				'userName': 'Vijay Pal',
				'tripFrom': 'Noida',
				'tripTo': 'Agra',
				'startTime': '02:00pm',
				
			},
			{
				'tripId': 1865,
				'driverName': 'Hemant Gusain',
				'userName': 'Vijay Pal',
				'tripFrom': 'Noida',
				'tripTo': 'Agra',
				'startTime': '02:00pm',
				
			}
		]
	}

}
