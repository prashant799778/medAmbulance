import { Component, OnInit } from '@angular/core';
import { UserService } from 'src/app/services/user.service';
import { AppSettings } from 'src/app/utils/constant';
import { Router } from '@angular/router';

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
	constructor(public userService: UserService,public router: Router) { }

	ngOnInit() {
		this.getFareList()
	}

	getFareList(){
		let data={
			'startLimit': 0,
			'endLimit': 10
		}
		this.userService.dataPostApi(data,AppSettings.getFareManagement).then(resp=>{
			if(resp['status']=='true'){
				this.fareListData = resp['result']
			}
		})

		// this.fareListData = [
		// 	{	'vehicleType':'CNG',
		// 		'farePerKM': 10,
		// 		'minFare': 100,
		// 		'minDistance': 5,
		// 		'waitingFare': 100,
				
		// 	},
		// 	{	'vehicleType':'Petrol',
		// 		'farePerKM': 25,
		// 		'minFare': 100,
		// 		'minDistance': 5,
		// 		'waitingFare': 100,
				
		// 	},
		// 	{	'vehicleType':'Desile',
		// 		'farePerKM': 20,
		// 		'minFare': 100,
		// 		'minDistance': 5,
		// 		'waitingFare': 100,
				
		// 	}
		// ]
	}
	editFare(id){
		this.router.navigate(['/fare/addFare'],{queryParams:{id:id}})
	}

}
