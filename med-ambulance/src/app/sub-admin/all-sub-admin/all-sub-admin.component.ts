import { Component, OnInit } from '@angular/core';
import { UserService } from 'src/app/services/user.service';
import { AppSettings } from 'src/app/utils/constant';
import { Router } from '@angular/router';
declare var jQuery: any;

@Component({
  selector: 'app-all-sub-admin',
  templateUrl: './all-sub-admin.component.html',
  styleUrls: ['./all-sub-admin.component.css']
})
export class AllSubAdminComponent implements OnInit {
	hospitalList = []
	Id: any;
	activatedds: boolean;
	stattus: number;
	constructor(public userService: UserService,
				public router: Router ) { }

	ngOnInit() {
		this.userService.hospitalAdminEventEmit.subscribe(()=>{
			this.getHospitalData()
		})
		this.getHospitalData()
	}

	getHospitalData(){
		let data = {
			'startLimit': 0,
			'endLimit': 10
		}
		this.userService.dataPostApi(data,AppSettings.allhospitalUserMaster).then(resp=>{
			if(resp['status'] == 'true'){
				this.hospitalList = resp['result']
			}
		})
	}

	getGender(id){
		if(id == 0){
			return 'Male'
		}else if(id == 1){
			return 'female'
		}
	}

	editAdmin(id,view){
		this.router.navigate(['/admin/addAdmin'],{queryParams: {Id : id, view: view}})

	}

	VerifyDriver(){
		let data = {
			'Id': this.Id
		}
		this.userService.dataPostApi(data,AppSettings.updateHospitalAdminStatus).then(resp=>{
			if(resp['status'] == 'true'){
				let data = {
					'startLimit': 0,
					'endLimit': 10
				}
				this.userService.dataPostApi(data,AppSettings.allhospitalUserMaster).then(resp=>{
					if(resp['status'] == 'true'){
				
						// this.errorMessage = false;
						this.hospitalList = resp['result']
						// this.loader = false;
					}else{
							// this.errorMessage = true;
							// this.messageShow = resp['message']
							// this.loader = false;
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
	verifiedDriver(id,status){
		this.Id = id;
		if(status == 0){
			this.stattus = 0
		}else{
			this.stattus = 1
		}
		jQuery('#verifiyModal').modal('show')
	}
	closeModal(){
		jQuery('#verifiyModal').modal('hide')
	}

	deleteDriver(id){
		this.userService.deleteData('Hospital Admin',id)
		
		jQuery('#deleteModal').modal('show')
	}
}
