from celery import shared_task
from .models import Author, Book, BorrowRecord
import os
import json
from datetime import datetime

@shared_task
def generate_report():
    reports_dir = 'reports'
    if not os.path.exists(reports_dir):
        os.makedirs(reports_dir)
    report = {
        'total_authors': Author.objects.count(),
        'total_books': Book.objects.count(),
        'total_books_borrowed': BorrowRecord.objects.filter(return_date__isnull=True).count(),
    }
    timestamp = datetime.now().strftime('%Y%m%d')
    filename = f'report_{timestamp}.json'
    with open(os.path.join(reports_dir, filename), 'w') as f:
        json.dump(report, f)
