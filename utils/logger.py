import logging

def setup_logger():
    """Configure and return the main logger"""
    logger = logging.getLogger('aws_resource_manager')
    if not logger.handlers:
        logger.setLevel(logging.INFO)
        
        # Create console handler
        handler = logging.StreamHandler()
        handler.setLevel(logging.INFO)
        
        # Create formatter
        formatter = logging.Formatter(
            '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
        )
        handler.setFormatter(formatter)
        
        # Add handler to logger
        logger.addHandler(handler)
    
    return logger

def get_logger():
    """Get the configured logger"""
    return logging.getLogger('aws_resource_manager')