import { Component, OnInit } from '@angular/core';
import { UserService } from '../services/user.service';
import { AppSettings } from '../utils/constant';

@Component({
  selector: 'app-dashboard',
  templateUrl: './dashboard.component.html',
  styleUrls: ['./dashboard.component.css']
})
export class DashboardComponent implements OnInit {
  
	constructor(public userService: UserService) { }

	ngOnInit() {
		this.userService.getApiData(AppSettings.alldriver).then(resp=>{
			console.log(resp)
		})
	}

}
