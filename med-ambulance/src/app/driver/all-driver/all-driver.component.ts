import { Component, OnInit } from '@angular/core';
import { UserService } from 'src/app/services/user.service';
import { AppSettings } from 'src/app/utils/constant';
import { Router } from '@angular/router';
// import { driverEventEmit } from '../../app.component'
declare var jQuery: any;

@Component({
  selector: 'app-all-driver',
  templateUrl: './all-driver.component.html',
  styleUrls: ['./all-driver.component.css']
})
export class AllDriverComponent implements OnInit {
	 
	driverData= []
	errorMessage: boolean
	messageShow: any;
	loader: boolean;
	activatedds: boolean;
	driverID: any;

	pageSize: any;
	totalRecords: any;
	paginationDisplay: boolean;

	constructor(public userService: UserService,
				public router: Router) { 
		this.errorMessage = false;
		this.loader = true;
		this.activatedds;
		this.pageSize = 10;
	}

	ngOnInit() {
		this.userService.driverEventEmit.subscribe(()=>{
			this.getDriverData()
		})
		this.getDriverData()
	}

	getDriverData(){
		let data = {
			'startLimit': 0,
			'endLimit': 10
		}
		this.userService.dataPostApi(data,AppSettings.alldriver).then(resp=>{
			if(resp['status'] == 'true'){
				
				// this.errorMessage = false;
				// this.driverData = resp['result']



				// if(resp['status'] == 'true'){
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
					// this.loader = false;
				



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

	editDriver(id,view){
		console.log(id)
		this.router.navigate(['/driver/editDriver'],{queryParams: {driverId : id, view: view}})
	}
	deleteDriver(id){
		this.userService.deleteData('Driver',id)
		
		jQuery('#deleteModal').modal('show')
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
		
		this.userService.dataPostApi(data,AppSettings.alldriver).then((data: any[]) => {
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

	VerifyDriver(){
		let data = {
			'driverId': this.driverID
		}
		this.userService.dataPostApi(data,AppSettings.updateDriverStatus).then(resp=>{
			if(resp['status'] == 'true'){
				let data = {
					'startLimit': 0,
					'endLimit': 10
				}
				this.userService.dataPostApi(data,AppSettings.alldriver).then(resp=>{
					if(resp['status'] == 'true'){
				
						this.errorMessage = false;
						this.driverData = resp['result']
						this.loader = false;
					}else{
							this.errorMessage = true;
							this.messageShow = resp['message']
							this.loader = false;
					}		
				})
				this.activatedds = true;
				setTimeout(() => {
					jQuery('#verifiyModal').modal('hide')
					setTimeout(()=>{
						this.activatedds = false;
					},1000)
				}, 2000);
			}
		})
	}
	verifiedDriver(id){
		this.driverID = id;
		jQuery('#verifiyModal').modal('show')
	}
	closeModal(){
		jQuery('#verifiyModal').modal('hide')
	}

}
