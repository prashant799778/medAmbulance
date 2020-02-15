import { Component, OnInit } from '@angular/core';

@Component({
  selector: 'app-booked-trip',
  templateUrl: './booked-trip.component.html',
  styleUrls: ['./booked-trip.component.css']
})
export class BookedTripComponent implements OnInit {
	tableHeading = [
		"No", "Trip Id", "Driver Name", "Passenger Name","Trip From", "Trip To","Allocated Driver","Start Time","Action"
	]
	heading='Booked Trip'
	constructor() { }

	ngOnInit() {
	}

}
