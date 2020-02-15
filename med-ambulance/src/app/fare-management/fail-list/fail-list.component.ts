import { Component, OnInit } from '@angular/core';

@Component({
  selector: 'app-fail-list',
  templateUrl: './fail-list.component.html',
  styleUrls: ['./fail-list.component.css']
})
export class FailListComponent implements OnInit {
	tableHeading = [
		"No", "Vehicle Type", "Fare Per KM", "Minimum Fare","Minimum Fare", "Minimum Distance","Waiting Fare","Action"
	]
	heading='Fare List'
	constructor() { }

	ngOnInit() {
	}

}
