import { Component, OnInit } from '@angular/core';
import { UserService } from 'src/app/services/user.service';
import { AppSettings } from 'src/app/utils/constant';

@Component({
  selector: 'app-booked-trip',
  templateUrl: './booked-trip.component.html',
  styleUrls: ['./booked-trip.component.css']
})
export class BookedTripComponent implements OnInit {
	tableHeading = [
		"No", "Trip Id", "Driver Name", "Passenger Name","Trip From", "Trip To","Start Time"
	]
	heading='Booked Trip'
	bookTripData = []
	constructor(public userService: UserService) { }

	ngOnInit() {
		this.getBookTrip()
	}

	getBookTrip(){
		let data = {
			'startLimit': 0,
			'endLimit': 10
		}
		this.userService.dataPostApi(data,AppSettings.bookedTrip).then(resp=>{
			this.bookTripData = resp['result']
		})
	}

}
