import { Component, OnInit } from '@angular/core';
import { UserService } from 'src/app/services/user.service';
import { AppSettings } from 'src/app/utils/constant';
import { FormGroup, FormBuilder } from '@angular/forms';
import { ActivatedRoute } from '@angular/router';
declare var jQuery: any;

@Component({
  selector: 'app-add-sub-admin',
  templateUrl: './add-sub-admin.component.html',
  styleUrls: ['./add-sub-admin.component.css']
})
export class AddSubAdminComponent implements OnInit {
	hospitalList = []
	hospitalForm: FormGroup;
	Id: any;
	views: boolean;
	viewEdit: any;
	addhosp: any;
	constructor(public userService: UserService,
				public route: ActivatedRoute,
				public fb:FormBuilder) { 
		this.createTable()
	}

	ngOnInit() {
		this.route.queryParams.subscribe(params => {
			this.Id = params['Id'];
			console.log(params['view'])
			// let vie = 
			if( params['view'] == 'view'){
				this.views= false;
				this.viewEdit = 'View'
				this.addhosp = 0
				this.disableForm()

			}else if(params['view'] == 'edit'){

				this.views = true;
				this.viewEdit = 'Edit'
				this.addhosp = 1
				// this.disableForm()
			}else{
				this.addhosp = 1
			}
			let data = {
				'Id': this.Id
			}
			this.userService.dataPostApi(data,AppSettings.allhospitalUserMaster).then(resp=>{
				this.setData(resp)
			})
		})	
		
		this.getHospital()
	}

	setData(resp){
		this.hospitalForm.get('name').setValue(resp['result'][0].name)
		this.hospitalForm.get('email').setValue(resp['result'][0].email)
		this.hospitalForm.get('gender').setValue(resp['result'][0].gender)
		this.hospitalForm.get('mobileNo').setValue(resp['result'][0].mobileNo)
		this.hospitalForm.get('password').setValue(resp['result'][0].password)
		this.hospitalForm.get('hospitalId').setValue(resp['result'][0].hospitalId)
		this.hospitalForm.get('userId').setValue(resp['result'][0].userId)
	}

	disableForm(){
		this.hospitalForm.disable()
	}

	getHospital(){
		this.userService.getApiData(AppSettings.hospitalMaster).then(resp=>{
			if(resp['status'] == 'true'){
				this.hospitalList = resp['result']
			}	
		})
	}
	createTable(){
		this.hospitalForm = this.fb.group({
			Id: [''],
			name: [''],
			gender: [''],
			mobileNo: [''],
			email: [''],
			password: [''],
			hospitalId: [''],
			userTypeId: [''],
			userId: ['']
		})
	}

	resetForm(){
		this.hospitalForm.reset()
	}

	submitData(){
		this.hospitalForm.get('userTypeId').setValue(5)
		let data = this.hospitalForm.getRawValue();
		this.userService.dataPostApi(data,AppSettings.addHospitalAdmin).then(resp=>{
			if(resp['status'] == 'true'){
				this.userService.messageValue('Hospital Admin added successfully')
				jQuery("#mainModal").modal('show')
				setTimeout(() => {
					jQuery('#mainModal').modal('hide')
				}, 2000);
				this.hospitalForm.reset();
			}
		})
	}

	updateData(){
		this.hospitalForm.get('Id').setValue(this.Id)
		this.hospitalForm.get('userTypeId').setValue(5)
		let data = this.hospitalForm.getRawValue();
		this.userService.dataPostApi(data,AppSettings.updateHospitalAdmin).then(resp=>{
			if(resp['status'] == 'true'){
				this.userService.messageValue('Hospital Admin Update successfully')
				jQuery("#mainModal").modal('show')
				setTimeout(() => {
					jQuery('#mainModal').modal('hide')
				}, 2000);
				this.hospitalForm.reset();
				let data = {
					'Id': this.Id
				}
				this.userService.dataPostApi(data,AppSettings.allhospitalUserMaster).then(resp=>{
					this.setData(resp)
				})
			}
		})
	}

	
}
