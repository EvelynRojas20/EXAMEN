import { TestBed } from '@angular/core/testing';

import { PPService } from './pp.service';

describe('PPService', () => {
  let service: PPService;

  beforeEach(() => {
    TestBed.configureTestingModule({});
    service = TestBed.inject(PPService);
  });

  it('should be created', () => {
    expect(service).toBeTruthy();
  });
});
