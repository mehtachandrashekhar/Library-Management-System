from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.decorators import action
from .models import Author, Book, BorrowRecord
from .serializers import AuthorSerializer, BookSerializer, BorrowRecordSerializer
from datetime import date
import os
import json

class AuthorViewSet(viewsets.ModelViewSet):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer

class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

class BorrowRecordViewSet(viewsets.ModelViewSet):
    queryset = BorrowRecord.objects.all()
    serializer_class = BorrowRecordSerializer

    def create(self, request, *args, **kwargs):
        book_id = request.data.get('book')
        book = Book.objects.get(id=book_id)
        if book.available_copies > 0:
            book.available_copies -= 1
            book.save()
            return super().create(request, *args, **kwargs)
        else:
            return Response({'error': 'No available copies'}, status=status.HTTP_400_BAD_REQUEST)

    @action(detail=True, methods=['put'], url_path='return')
    def mark_as_returned(self, request, pk=None):
        borrow_record = self.get_object()
        borrow_record.return_date = date.today()
        borrow_record.book.available_copies += 1
        borrow_record.book.save()
        borrow_record.save()
        return Response(BorrowRecordSerializer(borrow_record).data)

class ReportViewSet(viewsets.ViewSet):
    def list(self, request):
        reports_dir = 'reports'
        if not os.path.exists(reports_dir):
            return Response({'error': 'No reports found'}, status=status.HTTP_404_NOT_FOUND)
        files = sorted(os.listdir(reports_dir))
        if files:
            with open(os.path.join(reports_dir, files[-1])) as f:
                report = json.load(f)
            return Response(report)
        else:
            return Response({'error': 'No reports found'}, status=status.HTTP_404_NOT_FOUND)

    def create(self, request):
        generate_report.delay()
        return Response({'message': 'Report generation initiated'}, status=status.HTTP_202_ACCEPTED)
