import { Component, OnInit } from '@angular/core';

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
	constructor() { }

	ngOnInit() {
		this.getActiveTripData()	
	}

	getActiveTripData(){
		this.activeTripData = [
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
