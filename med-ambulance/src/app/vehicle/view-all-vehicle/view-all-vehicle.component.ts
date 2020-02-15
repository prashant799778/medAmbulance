import { Component, OnInit } from '@angular/core';
import { UserService } from 'src/app/services/user.service';
import { AppSettings } from 'src/app/utils/constant';

@Component({
  selector: 'app-view-all-vehicle',
  templateUrl: './view-all-vehicle.component.html',
  styleUrls: ['./view-all-vehicle.component.css']
})
export class ViewAllVehicleComponent implements OnInit {
	vehicleData = []
	loader: boolean;
	totalRecords: any;
	pageSize: any;
	paginationDisplay: boolean;
	constructor(public userService: UserService) {
		this.loader = true;
	 }

	ngOnInit() {
		this.getVehicleData()
	}

	getVehicleData(){
		this.userService.getApiData(AppSettings.selectambulanceMaster).then(resp=>{
			if(resp['status'] == 'true'){
				this.vehicleData = resp['result']
				this.loader = false;
			}
		})
	}

	pageChanged(event){
		let endlimit = this.pageSize;
		let startlimit = (this.pageSize * event) - this.pageSize;
		if(endlimit > this.totalRecords){
			endlimit = this.totalRecords;
			console
			// this.frmShowNews.get('endlimit').setValue(endlimit)
		}else{
			endlimit = this.pageSize
		}
		// this.frmShowNews.get('startlimit').setValue(startlimit)
		let data = {
			'endlimit': endlimit,
			'startlimit': startlimit
		}
		this.userService.dataPostApi(data,AppSettings.selectambulanceMaster).then((data: any[]) => {
			this.totalRecords = data['totalCount']
			if(this.totalRecords > this.pageSize){
				this.paginationDisplay = true;
			}else{
				this.paginationDisplay = false;
			}
			this.vehicleData = data['result']
			this.loader = false;
			
		});
	}

}
