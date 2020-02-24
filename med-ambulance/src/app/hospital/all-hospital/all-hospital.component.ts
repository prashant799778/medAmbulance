import { Component, OnInit } from '@angular/core';
import { UserService } from 'src/app/services/user.service';
import { Router } from '@angular/router';
import { AppSettings } from 'src/app/utils/constant';
declare var jQuery: any;

@Component({
  selector: 'app-all-hospital',
  templateUrl: './all-hospital.component.html',
  styleUrls: ['./all-hospital.component.css']
})
export class AllHospitalComponent implements OnInit {
	driverData= []
	errorMessage: boolean
	messageShow: any;
	loader: boolean;
	pageSize: any;
	totalRecords: any;
	paginationDisplay: boolean;
	constructor(public userService: UserService,
				public router: Router) { 
		this.errorMessage = false;
		this.loader = true;
		this.pageSize = 10;
		
	}

	ngOnInit() {
		this.userService.hospitalEventEmit.subscribe(()=>{
			this.getDriverData()
		})
		this.getDriverData()
	}

	getDriverData(){
		let data = {
			'startLimit': 0,
			'endLimit': 10
		}
		this.userService.dataPostApi(data,AppSettings.allHospital).then(resp=>{
			if(resp['status'] == 'true'){
				this.totalRecords = resp['totalCount']
				// this.totalRecords = 15;
				if(this.totalRecords > this.pageSize){
				  console.log("inside if",this.totalRecords)
				  this.paginationDisplay = true;
				  }else{
					console.log("inside else",this.totalRecords)
				  this.paginationDisplay = false;
				  }
				
				this.errorMessage = false;
				this.driverData = resp['result']
				this.loader = false;
			}else{
					this.errorMessage = true;
					this.messageShow = resp['message']
					this.loader = false;
				
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

	pageChanged(event){
		console.log(event)
		// this.pageSize = event;
		// let totalpagess = (this.totalRecords / 2)
		let endlimit = this.pageSize;
		let startlimit = (this.pageSize * event) - this.pageSize;
		if(endlimit > this.totalRecords){
		endlimit = this.totalRecords;
		
		}else{
			endlimit = this.pageSize;
		}
		
		let data = {
			'startLimit': startlimit,
			'endLimit': endlimit
		}
		
		this.userService.dataPostApi(data,AppSettings.allHospital).then((data: any[]) => {
		  this.totalRecords = data['totalCount']
		  console.log(this.totalRecords)
		  if(this.totalRecords > this.pageSize){
			console.log("inside if",this.totalRecords)
			this.paginationDisplay = true;
			}else{
			  console.log("inside else",this.totalRecords)
			this.paginationDisplay = false;
			}
		  this.driverData = data['result'];
		  
		});
		}

	editHospital(id,view){
		console.log(id)
		this.router.navigate(['/hospital/editHospital'],{queryParams: {id : id, view: view}})
	}
	deleteHospital(id){
		this.userService.deleteData('Hospital',id)
		
		jQuery('#deleteModal').modal('show')
	}

}