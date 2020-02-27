import { Component, OnInit } from '@angular/core';
import { UserService } from 'src/app/services/user.service';
import { AppSettings } from 'src/app/utils/constant';
import { LocalStorageService } from 'angular-web-storage';

@Component({
  selector: 'app-hospital-past-booking',
  templateUrl: './hospital-past-booking.component.html',
  styleUrls: ['./hospital-past-booking.component.css']
})
export class HospitalPastBookingComponent implements OnInit {
	hospitalID: any;
	pastRideData
	constructor(public userService: UserService,
				public local: LocalStorageService) { }

	ngOnInit() {
		
		if(this.local.get('userData1') && this.local.get('userData1').hospitalId){
			this.hospitalID = this.local.get('userData1').hospitalId
			this.getPastBookingData()
		}
	}

	getPastBookingData(){
		let data = {
			'hospitalId': this.hospitalID
		}
		this.userService.dataPostApi(data,AppSettings.pastBooking).then(resp=>{
			if(resp['status'] == 'true'){
				this.pastRideData = resp['result']
			}
		})
		
	}
}
