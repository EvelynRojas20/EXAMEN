import { HttpClient } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { Observable} from 'rxjs';

@Injectable({
  providedIn: 'root'
})
export class PPService {

  constructor(private http: HttpClient) { }

  public test():Observable<any>{
    return this.http.get("http://localhost:8000/users")
  }
}
