import { Component, OnInit } from '@angular/core';
import { UserService } from 'src/app/services/user.service';
import { AppSettings } from 'src/app/utils/constant';

@Component({
  selector: 'app-all-driver',
  templateUrl: './all-driver.component.html',
  styleUrls: ['./all-driver.component.css']
})
export class AllDriverComponent implements OnInit {
	tableHeading = [
		"No", "Name", "Mobile", "Email","Address", "Joining Date","Trip","Status","Action"
	]
	heading='All Driver'
	driverData= []
	constructor(public userService: UserService) { }

	ngOnInit() {
		this.getDriverData()
	}

	getDriverData(){
		this.userService.getApiData(AppSettings.alldriver).then(resp=>{
			if(resp['status'] == 'true'){
				this.driverData = resp['result']
			}
		})
	}

	getStatus(status){
		if(status == 0){
			return 'ON TRIP'
		}else if(status == 1){
			return 'AVAILABLE'
		}else if(status == 2){
			return 'LEAVE'
		}

	}

}
