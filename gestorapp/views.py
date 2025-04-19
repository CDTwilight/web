from django.shortcuts import render
from pedidos.models import Pedido, PedidoDetalle
from inventario.models import Material
from django.contrib.auth.models import User
from django.db.models import Sum, Count, Avg, Max, F, FloatField, Q
from django.db.models.functions import Cast, TruncMonth
from django.utils import timezone
from datetime import datetime, timedelta




# Create your views here.

def home(request):
    # Calcular total de ventas (pedidos efectuados)
    total_ventas = Pedido.objects.filter(
        estado='efectuado'  # Changed from efectuado=True
    ).aggregate(
        total=Sum('total')
    )['total'] or 0

    # Obtener total de productos en stock
    total_productos = Material.objects.aggregate(
        total=Sum('cantidad')
    )['total'] or 0

    # Obtener número de clientes activos (usuarios que han hecho pedidos en el último mes)
    mes_anterior = timezone.now() - timedelta(days=30)
    clientes_activos = Pedido.objects.filter(
        created_at__gte=mes_anterior
    ).values('user').distinct().count()

    context = {
        'total_ventas': f"${total_ventas:,.2f}",
        'total_productos': total_productos,
        'total_clientes': clientes_activos
    }

    return render(request, "gestorapp/home.html", context)



def registro(request):
    
    return render(request, "gestorapp/registro.html")

def analytics_dashboard(request):
    # Obtener el primer día del mes actual
    today = timezone.now()
    primer_dia_mes = today.replace(day=1, hour=0, minute=0, second=0, microsecond=0)
    
    # Obtener estadísticas mensuales de materiales
    materiales_stats = Material.objects.annotate(
        # Ventas del mes actual
        ventas_totales=Sum(
            'pedidodetalle__cantidad',
            filter=Q(
                pedidodetalle__pedido__estado='efectuado',
                pedidodetalle__pedido__created_at__gte=primer_dia_mes
            ),
            default=0
        ),
        # Stock total (actual + vendido en el mes)
        stock_total=F('cantidad') + F('ventas_totales'),
        # Ingresos del mes
        ingresos_total=Sum(
            F('pedidodetalle__cantidad') * F('precio'),
            filter=Q(
                pedidodetalle__pedido__estado='efectuado',
                pedidodetalle__pedido__created_at__gte=primer_dia_mes
            ),
            default=0
        ),
        pedidos_pendientes=Sum(
        'pedidodetalle__cantidad',
        filter=Q(
            pedidodetalle__pedido__estado='pendiente'
        ),
        default=0
    ),
        stock_total_m_pendientes=F('cantidad') + F('ventas_totales') + F('pedidos_pendientes'),

        # Porcentaje de ventas respecto al stock total del mes
        porcentaje_ventas=Cast(
            100 * Cast(
                F('ventas_totales'),
                FloatField()
            ) / Cast(
                F('stock_total_m_pendientes'),
                FloatField()
            ),
            FloatField()
        )
    ).order_by('-ventas_totales')

    context = {
        'materiales': materiales_stats,
        'mes_actual': today.strftime('%B %Y')
    }
    
    return render(request, 'gestorapp/analytics.html', context)
