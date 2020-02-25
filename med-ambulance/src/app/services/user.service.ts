import { Injectable, EventEmitter } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { SessionStorageService, LocalStorageService } from 'angular-web-storage';

@Injectable({
  providedIn: 'root'
})
export class UserService {
  baseUrl= 'http://134.209.153.34:5077/';
	user: any;
	KEY = 'value';
	superLogin: boolean;
	messageResult: any;
	imageZoomPath: any;
	deleteDataName: any;
	deletDataId: any;
	driverEventEmit = new EventEmitter<any>();
	hospitalEventEmit = new EventEmitter<any>();
	hospitalAdminEventEmit = new EventEmitter<any>();
	constructor(private http: HttpClient,
				public local: LocalStorageService,
				public session: SessionStorageService) { }

	dataPostApi(data, endpoint){
		return  new Promise((resolve, reject) => {
			let url = this.baseUrl+endpoint;
			this.http.post(url,data).toPromise().then(res =>{
				if(res ){
					resolve(res);
				}else{
					reject('error')
				}
			});
		})
	}
	getApiDatawithData (endpoint,data){
		console.log(data)
		return  new Promise((resolve, reject) => {
			console.log(this.baseUrl, endpoint)
				let url = this.baseUrl+''+endpoint+'?userId='+data.userId;
				console.log(url)
				this.http.get(url).toPromise().then(res =>{
					if(res ){
						resolve(res);
					}else{
						reject('error')
					}
				});
			})
	}
	getApiData( endpoint){
		return  new Promise((resolve, reject) => {
			console.log(this.baseUrl, endpoint)
				let url = this.baseUrl+''+endpoint;
				console.log(url)
				this.http.get(url).toPromise().then(res =>{
					if(res ){
						resolve(res);
					}else{
						reject('error')
					}
				});
			})
	}
	getApiDataacountVerfication(endpoint, data){
		return  new Promise((resolve, reject) => {
			console.log(this.baseUrl, endpoint)
				let url = this.baseUrl+''+endpoint+'?userId='+data.userId;
				console.log(url)
				this.http.get(url).toPromise().then(res =>{
					if(res ){
						resolve(res);
					}else{
						reject('error')
					}
				});
			})
	}
	getSaveCustomer(data){
		console.log("data value",data)
		
		  this.user = data;
		  
		 
		  // this.session.set(this.KEY, data);
		  this.local.set('userData1',(data))
		//   this.local.set('userData2',(datas))
		//   this.session.set(this.KEY,this.local.get('userData1'))
		
	  }
	  getSaveCustomer1(data){
		console.log("data value",data)
		
		  this.user = data;
		  
		//   let datas = {
		// 	  	'superLogin': 'no'
		//   }
		  // this.session.set(this.KEY, data);
		//   this.local.set('userData1',(data))
		  this.local.set('userData2',(data))
		//   this.session.set(this.KEY,this.local.get('userData1'))
		
	  }

	  setSuperLogin(login){
			if(login == true){
				this.superLogin = true;
			}else{
				this.superLogin = false;
			}
	  }	

		messageValue(data){
			this.messageResult = data	
		}
	imagePath(path){
		this.imageZoomPath = path
	}	
	deleteData(deletDataName, id){
		this.deletDataId = id;
		this.deleteDataName = deletDataName
	}
	EmitEvnt(dataName){
		if(dataName == 'Driver'){
			this.driverEventEmit.emit();
		}else if(dataName == 'Hospital'){
			this.hospitalEventEmit.emit();
		}else if(dataName == 'Hospital Admin'){
			this.hospitalAdminEventEmit.emit();
		}
	}
}

