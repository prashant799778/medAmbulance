import { Component, OnInit } from '@angular/core';
import { UserService } from 'src/app/services/user.service';
import { FormGroup, FormBuilder } from '@angular/forms';
import {IMyDpOptions} from 'mydatepicker';

@Component({
  selector: 'app-add-vehicle',
  templateUrl: './add-vehicle.component.html',
  styleUrls: ['./add-vehicle.component.css']
})
export class AddVehicleComponent implements OnInit {
	vehicleForm: FormGroup;
	public myDatePickerOptions: IMyDpOptions = {
		dateFormat: 'dd.mm.yyyy',
	};
	file: any;
	imageShow: any;
	showBanner: number;
	
	constructor(public userService: UserService,
				public fb: FormBuilder) { 
		this.showBanner = 0;			
		this.createTable()
	}

	ngOnInit() {

	}
	createTable(){
		this.vehicleForm = this.fb.group({
			regNumber: [''],
			vehicleImage: [''],
			registrationDate: [''],
			manufacture: [''],
			fuelType: [''],
			modal: [''],
			type: [''],
			category: ['']
		})
	}

	onFileSelect(event) {
		console.log(event)
		if(event.type === "change"){
			if (event.target.files.length > 0) {
				this.file = event.target.files[0];
				var reader = new FileReader();
				reader.readAsDataURL(event.target.files[0]);
				reader.onload = (event) => {
					this.imageShow = (<FileReader>event.target).result;
					this.vehicleForm.get('vehicleImage').setValue(this.file);
					this.showBanner = 1;
				}
			}
		  
		}
		
		
	 
	  }
	

}
