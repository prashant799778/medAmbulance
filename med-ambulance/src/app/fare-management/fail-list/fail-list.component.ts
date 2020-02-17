import { Component, OnInit } from '@angular/core';

@Component({
  selector: 'app-fail-list',
  templateUrl: './fail-list.component.html',
  styleUrls: ['./fail-list.component.css']
})
export class FailListComponent implements OnInit {
	tableHeading = [
		"No", "Vehicle Type", "Fare Per KM", "Minimum Fare", "Minimum Distance","Waiting Fare","Action"
	]
	heading='Fare List'
	fareListData = []
	constructor() { }

	ngOnInit() {
		this.getFareList()
	}

	getFareList(){
		this.fareListData = [
			{	'vehicleType':'CNG',
				'farePerKM': 10,
				'minFare': 100,
				'minDistance': 5,
				'waitingFare': 100,
				
			},
			{	'vehicleType':'Petrol',
				'farePerKM': 25,
				'minFare': 100,
				'minDistance': 5,
				'waitingFare': 100,
				
			},
			{	'vehicleType':'Desile',
				'farePerKM': 20,
				'minFare': 100,
				'minDistance': 5,
				'waitingFare': 100,
				
			}
		]
	}

}
