import { Component, OnInit } from '@angular/core';
import { FormGroup, FormBuilder,Validators } from '@angular/forms';
import { AuthsService } from '../services/auths.service';
import { UserService } from '../services/user.service';
import { ActivatedRoute } from '@angular/router';
import { LocalStorageService } from 'angular-web-storage';
declare var jQuery: any;
@Component({
  selector: 'app-account',
  templateUrl: './account.component.html',
  styleUrls: ['./account.component.css']
})
export class AccountComponent implements OnInit {
  loginForm: FormGroup
  // fb: any;
  errors: string;
  showPasswords: boolean;
  // authsService: any;
  loginSuccess: boolean;
  lloginSuccess: boolean;
  // local: any;
  constructor(public fb: FormBuilder,
    public userService: UserService,
    public route: ActivatedRoute,
    public local: LocalStorageService,
    public authsService: AuthsService) { 
    this.createTable()
  }

  ngOnInit() {
  }
  createTable(){
		this.loginForm = this.fb.group({
			login: this.fb.group({
				email: ['',[Validators.required, Validators.pattern(/^[a-z0-9._%+-]+@[a-z0-9.-]+\.[a-z]{2,4}$/)]],
				password: ['',Validators.required],
				terms: ['']
				
      }),
	})
	this.loginForm.get('login').get('terms').valueChanges.subscribe(value =>{
		console.log(value)
		if(value == true){
			this.errors = ''
		}
	})
  }
	showPassword(id){
		if(this.showPasswords == true){
			this.showPasswords = false;
		}else{
			this.showPasswords = true;
		}
		
		
		// let passwor = this.loginForm.get('data').get('Password')
		// console.log(passwor)
		var x = document.getElementById(id);
		
		if (x['type'] === "password") {
			x['type'] = "text";
		} else {
			x['type'] = "password";
		}
	}
	getLogin(){
		// console.log("prashant ")
		if(this.loginForm.get('login').get('terms').value == false){
			this.errors = 'Please select the terms and conditions'
		}else{
      let userData = this.loginForm.get('login').value;
      console.log(userData)
			this.authsService.login(userData).subscribe(resp =>{

				if(resp['status'] == 'true'){
					if(resp['result'].userTypeId == 1 || resp['result'].userTypeId == 5){
						this.loginSuccess= true;
						this.getSaveCustomer(resp['result'])

					}else{
						this.errors = 'you are not authorized Admin'
					}
					
				}else{
					this.loginSuccess = false;
					this.errors = resp['message']
				}
			})
		}

		
			
	}
	getSaveCustomer(data){
		console.log("data value",data)
		// if(data != null){
		 
		  // this.session.set(this.KEY, data);
		  this.local.set('userData1',(data))
		  console.log(this.loginForm)
		  if(data.userTypeId == 1){
			let datas = {
				'superLogin': 'yes'
			}  
			this.local.set('userData2',(datas))
		  }
	}
	logout(){
		this.authsService.logout()
	}
	closeModal(){
		jQuery("#logout-pop").modal('hide')
	}
	

}
