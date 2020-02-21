import { Component, OnInit } from '@angular/core';
import { FormGroup, FormBuilder } from '@angular/forms';
import { IMyDpOptions } from 'mydatepicker';
import { UserService } from 'src/app/services/user.service';
import { AppSettings } from 'src/app/utils/constant';
import { Router, ActivatedRoute } from '@angular/router';
declare var jQuery: any;

@Component({
  selector: 'app-edit-hospital',
  templateUrl: './edit-hospital.component.html',
  styleUrls: ['./edit-hospital.component.css']
})
export class EditHospitalComponent implements OnInit {
  hospitalForm: FormGroup;
	ambType = []
	facityId = []
	hospitalId: any;
	viewEdit: any;
	views: boolean
	public myDatePickerOptions: IMyDpOptions = {
		dateFormat: 'dd.mm.yyyy',
	};
	
	constructor(public userService: UserService,
				public router: Router,
				public route: ActivatedRoute,
				public fb: FormBuilder) { 
		this.createTable()
		this.getCategory()
	}

	ngOnInit() {
    this.route.queryParams.subscribe(params => {
			this.hospitalId = params['hospitalId'];
			// let vie = 
			if( params['view'] == 'view'){
				this.views= false;
				this.viewEdit = 'View'
				this.disableForm()

			}else{
				this.views = true;
				this.viewEdit = 'Edit'
				this.disableForm()
			}
			let data = {
				'hospitalId': this.hospitalId
			}
			this.userService.dataPostApi(data,AppSettings.allHospital).then(resp=>{
				// this.setData(resp)
			})
		})	
	}
	createTable(){
		this.hospitalForm = this.fb.group({
			ambType: [''],
			name: [''],
			address: [''],
			lat: [''],
			lng: [''],
			facilityId: ['']
			
		})
	}
  
	disableForm(){
		this.hospitalForm.disable()
	}

	resetForm(){
		this.hospitalForm.reset();
	}

	submitData(){
		// if(resp['status'] == 'true'){
			console.log("modal")
				jQuery('#mainModal').modal('show')
				this.userService.messageValue('Hospital Inserted successfully')
				setTimeout(() => {
					jQuery('#mainModal').modal('hide')
				}, 2000000000);
		// }
	}
	getCategory(){
		this.userService.getApiData(AppSettings.facilityMaster).then(resp=>{
			this.facityId = resp['result'] 
		})
		this.userService.getApiData(AppSettings.selectambulanceTypeMaster).then(resp=>{
			this.ambType = resp['result']
		})
	}
}	