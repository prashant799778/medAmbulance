import { Component, OnInit } from '@angular/core';
import { UserService } from 'src/app/services/user.service';
import { AppSettings } from 'src/app/utils/constant';

@Component({
  selector: 'app-route-map',
  templateUrl: './route-map.component.html',
  styleUrls: ['./route-map.component.css']
})
export class RouteMapComponent implements OnInit {

  	constructor(public userService: UserService) { }

	ngOnInit() {
		this.getBookTrip()
	}

	getBookTrip(){
		let data = {
			'startLimit': 0,
			'endLimit': 10
		}
		this.userService.dataPostApi(data,AppSettings.cancelledTrip).then(resp=>{
			console.log(resp)
		})
	}

}
