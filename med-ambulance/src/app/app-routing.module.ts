import { NgModule } from '@angular/core';
import { Routes, RouterModule } from '@angular/router';
import { AuthGuard } from './services/auth.guard';
import { DashboardComponent } from './dashboard/dashboard.component';
import { ActiveTripComponent } from './trip/active-trip/active-trip.component';
import { BookedTripComponent } from './trip/booked-trip/booked-trip.component';
import { CompleteTripComponent } from './trip/complete-trip/complete-trip.component';
import { RouteMapComponent } from './trip/route-map/route-map.component';
import { AddDriverComponent } from './driver/add-driver/add-driver.component';
import { AllDriverComponent } from './driver/all-driver/all-driver.component';
import { DriverPaymentComponent } from './driver/driver-payment/driver-payment.component';
import { AllPassengersComponent } from './all-passengers/all-passengers.component';
import { AddVehicleComponent } from './vehicle/add-vehicle/add-vehicle.component';
import { ViewAllVehicleComponent } from './vehicle/view-all-vehicle/view-all-vehicle.component';
import { EditVehicleComponent } from './vehicle/edit-vehicle/edit-vehicle.component';
import { AddFareComponent } from './fare-management/add-fare/add-fare.component';
import { FailListComponent } from './fare-management/fail-list/fail-list.component';
import { EditDriverComponent } from './driver/edit-driver/edit-driver.component';
import { AllHospitalComponent } from './hospital/all-hospital/all-hospital.component';
import { EditHospitalComponent } from './hospital/edit-hospital/edit-hospital.component';
import { AddHospitalComponent } from './hospital/add-hospital/add-hospital.component';
import { AllResponderComponent } from './responder/all-responder/all-responder.component';
import { ViewResponderComponent } from './responder/view-responder/view-responder.component';
import { AddSubAdminComponent } from './sub-admin/add-sub-admin/add-sub-admin.component';
import { AdminDashboardComponent } from './sub-admin/admin-dashboard/admin-dashboard.component';
import { AllSubAdminComponent } from './sub-admin/all-sub-admin/all-sub-admin.component';
import { HospitalAccountComponent } from './hospital-admin/hospital-account/hospital-account.component';
import { HospitalPastBookingComponent } from './hospital-admin/hospital-past-booking/hospital-past-booking.component';
import { AllBikeComponent } from './bike/all-bike/all-bike.component';


const routes: Routes = [
	
	{ path: '',redirectTo: '/dashboard',pathMatch: 'full'},
	{ path: 'dashboard', component: DashboardComponent, canActivate:[AuthGuard]},
	{ path: 'allPassengers', component: AllPassengersComponent, canActivate:[AuthGuard]},
	{ path:'hospitalAdmin',component: HospitalAccountComponent,canActivate: [AuthGuard]},
	{ path:'pastRide',component: HospitalPastBookingComponent,canActivate: [AuthGuard]},
	{ path: 'trip',
		children: [                          //<---- child components declared here
	  		{ path: '',redirectTo: '/trip/activeTrip',pathMatch:'full'}, 
			{ path:'activeTrip',component: ActiveTripComponent,canActivate: [AuthGuard]},
			{ path:'bookedTrip',component: BookedTripComponent,canActivate: [AuthGuard]},
			{ path:'completeTrip',component: CompleteTripComponent,canActivate: [AuthGuard]},
			{ path:'cancelTrip',component: RouteMapComponent,canActivate: [AuthGuard]}
		]
	},
	{ path: 'driver',
		children: [                          //<---- child components declared here
	  		{ path: '',redirectTo: '/driver/allDriver',pathMatch:'full'}, 
			{ path:'addDriver',component: AddDriverComponent,canActivate: [AuthGuard]},
			{ path:'editDriver',component: EditDriverComponent,canActivate: [AuthGuard]},
			{ path:'allDriver',component: AllDriverComponent,canActivate: [AuthGuard]},
			{ path:'driverPayment',component: DriverPaymentComponent,canActivate: [AuthGuard]},
		]
	},
	{ path: 'responder',
		children: [                          //<---- child components declared here
	  		{ path: '',redirectTo: '/responder/allResponder',pathMatch:'full'}, 
			{ path:'viewResponder',component: ViewResponderComponent,canActivate: [AuthGuard]},
			{ path:'allResponder',component: AllResponderComponent,canActivate: [AuthGuard]},
		]
	},
	{ path: 'hospital',
		children: [                          //<---- child components declared here
	  		{ path: '',redirectTo: '/hospital/allHospital',pathMatch:'full'}, 
			{ path:'addHospital',component: AddHospitalComponent,canActivate: [AuthGuard]},
			{ path:'editHospital',component: EditHospitalComponent,canActivate: [AuthGuard]},
			{ path:'allHospital',component: AllHospitalComponent,canActivate: [AuthGuard]},
		]
	},
	{ path: 'vehicle',
		children: [                          //<---- child components declared here
	  		{ path: '',redirectTo: '/vehicle/addVehicle',pathMatch:'full'}, 
			{ path:'addVehicle',component: AddVehicleComponent,canActivate: [AuthGuard]},
			{ path:'allVehicle',component: ViewAllVehicleComponent,canActivate: [AuthGuard]},
			{ path:'editVehicle',component: EditVehicleComponent,canActivate: [AuthGuard]},
		]
	},
	{ path: 'bike',
		children: [                          //<---- child components declared here
	  		{ path: '',redirectTo: '/bike/allBike',pathMatch:'full'}, 
			{ path:'allBike',component: AllBikeComponent,canActivate: [AuthGuard]},
			// { path:'fareList',component: FailListComponent,canActivate: [AuthGuard]},
		]
	},
	{ path: 'fare',
		children: [                          //<---- child components declared here
	  		{ path: '',redirectTo: '/fare/addFare',pathMatch:'full'}, 
			{ path:'addFare',component: AddFareComponent,canActivate: [AuthGuard]},
			{ path:'fareList',component: FailListComponent,canActivate: [AuthGuard]},
		]
	},
	{ path: 'admin',
		children: [                          //<---- child components declared here
	  		{ path: '',redirectTo: '/admin/addAdmin',pathMatch:'full'}, 
			{ path:'addAdmin',component: AddSubAdminComponent,canActivate: [AuthGuard]},
			{ path:'adminDashboard',component: AdminDashboardComponent,canActivate: [AuthGuard]},
			{ path:'allAdmin',component: AllSubAdminComponent,canActivate: [AuthGuard]},
		]
	},
	
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
