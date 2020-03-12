import { Component, OnInit } from '@angular/core';
import { UserService } from 'src/app/services/user.service';
import { AppSettings } from 'src/app/utils/constant';

@Component({
  selector: 'app-route-map',
  templateUrl: './route-map.component.html',
  styleUrls: ['./route-map.component.css']
})
export class RouteMapComponent implements OnInit {
	tableHeading = [
		"No", "Driver Name", "Passenger Name","Trip From", "Trip To","Start Time"
	]
	heading='Cancelled Trips'
	cancelTripData = []
  	constructor(public userService: UserService) { }

	ngOnInit() {
		this.getBookTrip()
	}

	getBookTrip(){
		let data = {
			'startLimit': 0,
			'endLimit': 10
		}
		// this.userService.dataPostApi(data,AppSettings.cancelledTrip).then(resp=>{
		// 	console.log(resp)
		// })
		this.cancelTripData = [
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
