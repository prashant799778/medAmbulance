import { Component, OnInit } from '@angular/core';

@Component({
  selector: 'app-driver-payment',
  templateUrl: './driver-payment.component.html',
  styleUrls: ['./driver-payment.component.css']
})
export class DriverPaymentComponent implements OnInit {
	tableHeading = [
		"No", "Transaction Id", "Name", "Date","Amount","Status","Commission","Action"
	]
	heading='Driver Payment'
	constructor() { }

	ngOnInit() {
	}

}
