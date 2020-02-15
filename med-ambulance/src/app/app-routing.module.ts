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


const routes: Routes = [
	{ path: '',redirectTo: '/dashboard',pathMatch: 'full'},
	{ path: 'dashboard', component: DashboardComponent, canActivate:[AuthGuard]},
	{ path: 'allPassengers', component: AllPassengersComponent, canActivate:[AuthGuard]},
	{ path: 'trip',
		children: [                          //<---- child components declared here
	  		{ path: '',redirectTo: '/trip/activeTrip',pathMatch:'full'}, 
			{ path:'activeTrip',component: ActiveTripComponent,canActivate: [AuthGuard]},
			{ path:'bookedTrip',component: BookedTripComponent,canActivate: [AuthGuard]},
			{ path:'completeTrip',component: CompleteTripComponent,canActivate: [AuthGuard]},
			{ path:'routeMap',component: RouteMapComponent,canActivate: [AuthGuard]}
		]
	},
	{ path: 'driver',
		children: [                          //<---- child components declared here
	  		{ path: '',redirectTo: '/driver/addDriver',pathMatch:'full'}, 
			{ path:'addDriver',component: AddDriverComponent,canActivate: [AuthGuard]},
			{ path:'allDriver',component: AllDriverComponent,canActivate: [AuthGuard]},
			{ path:'driverPayment',component: DriverPaymentComponent,canActivate: [AuthGuard]},
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
	{ path: 'fare',
		children: [                          //<---- child components declared here
	  		{ path: '',redirectTo: '/fare/addFare',pathMatch:'full'}, 
			{ path:'addFare',component: AddFareComponent,canActivate: [AuthGuard]},
			{ path:'fareList',component: FailListComponent,canActivate: [AuthGuard]},
		]
	},
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
