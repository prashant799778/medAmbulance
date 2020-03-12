import { Component, OnInit } from '@angular/core';
import { FormGroup, FormBuilder } from '@angular/forms';
import { IMyDpOptions } from 'mydatepicker';
import { UserService } from 'src/app/services/user.service';
import { AppSettings } from 'src/app/utils/constant';
import { ActivatedRoute } from '@angular/router';
declare var jQuery: any;

@Component({
  selector: 'app-add-fare',
  templateUrl: './add-fare.component.html',
  styleUrls: ['./add-fare.component.css']
})
export class AddFareComponent implements OnInit {
  vehicleForm: FormGroup;
  ambType=[];
  id: any;
;	public myDatePickerOptions: IMyDpOptions = {
		dateFormat: 'dd.mm.yyyy',
	};
	
	constructor(public userService: UserService,
				public route: ActivatedRoute,
				public fb: FormBuilder) { 
		this.createTable()
	}

	ngOnInit() {
		this.userService.getApiData(AppSettings.selectambulanceMode).then(resp=>{
			if(resp['status']=='true'){
				this.ambType =  resp['result']
			}
		})
		this.route.queryParams.subscribe(params => {
			this.id = params['id']; 
			if(this.id){
				this.getFareSetValue()
			}
			
		})
		
	}
	createTable(){
		this.vehicleForm = this.fb.group({
			ambType: [''],
			minFare: [''],
			minDistance: [''],
			waitFare: [''],
			farePerKM: [''],
		})
	}

	resetForm(){
		this.vehicleForm.reset();
	}

	submitData(){
		let data = this.vehicleForm.getRawValue();
		this.userService.dataPostApi(data,AppSettings.addFare).then(resp=>{
			if(resp['status']== 'true'){
				jQuery('#mainModal').modal('show')
				this.userService.messageValue('Fare Inserted successfully')
			}
		})
		
	}

	getFareSetValue(){
		let id=  {
			'id':this.id
		};
		this.userService.dataPostApi(id,AppSettings.getFareManagement).then(resp=>{
			if(resp['status']='true'){
				let fareValue = resp['result'][0]
				this.vehicleForm.get('ambType').setValue(fareValue.ambType)
				this.vehicleForm.get('minFare').setValue(fareValue.minFare)
				this.vehicleForm.get('minDistance').setValue(fareValue.minDistance)
				this.vehicleForm.get('waitFare').setValue(fareValue.waitFare)
				this.vehicleForm.get('farePerKM').setValue(fareValue.farePerKM)
			}
		})
	}

	

}
