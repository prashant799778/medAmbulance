import { Component, OnInit } from '@angular/core';
import { UserService } from '../services/user.service';
import { AppSettings } from '../utils/constant';

@Component({
  selector: 'app-dashboard',
  templateUrl: './dashboard.component.html',
  styleUrls: ['./dashboard.component.css']
})
export class DashboardComponent implements OnInit {
	reviewData = []
	constructor(public userService: UserService) { }

	ngOnInit() {
		this.userService.getApiData(AppSettings.alldriver).then(resp=>{
			console.log(resp)
		})
		this.reviewData = 	[ 
								{
									'userImage': 'http://radixtouch.in/templates/templatemonster/ecab/source/assets/img/user/usrbig1.jpg',
									'name': 'Nisha',
									'review':'Good Serivces',
									'email': 'nisha@gmail.com',
									'star': 4
								},
								{
									'userImage': 'http://radixtouch.in/templates/templatemonster/ecab/source/assets/img/user/usrbig1.jpg',
									'name': 'Vijay',
									'review':'Good Serivces',
									'email': 'nisha@gmail.com',
									'star': 4
								},
								{
									'userImage': 'http://radixtouch.in/templates/templatemonster/ecab/source/assets/img/user/usrbig1.jpg',
									'name': 'Hemant',
									'review':'Good Serivces',
									'email': 'nisha@gmail.com',
									'star': 4
								}
							]
	}

}
