import { Component, OnInit } from '@angular/core';

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
	constructor() { }

	ngOnInit() {
	}

}
